import pymongo
import argparse
from .reducers import reducers
import sys

def accumulate_entries(hashmap, entries, args):
    for entry in entries:
        bucket = None
        skip = False
        for param in args.parameters:
            if param not in entry["config"]:
                if args.missing == "drop":
                    sys.stderr.write("Dropping experiment id:%d (parameter %s not found) \n" % (entry["_id"], param))
                    skip = True
                    break
                else:
                    entry["config"][param] = args.missing
                    sys.stderr.write("Overwriting experiment id:%d (parameter %s) \n" % (entry["_id"], param))
            
        if skip:
            continue

        bucket = "_".join([str(entry["config"][param]) for param in args.parameters])

        if bucket not in hashmap:
            hashmap[bucket] = dict((acc,[]) for acc in args.accumulate)
            hashmap[bucket]["results"] = []
        
        hashmap[bucket]["results"].append(entry["result"])
        for acc in args.accumulate:
            try:
                hashmap[bucket][acc].append(entry["info"][acc])
            except:
                sys.stderr.write("Skipping info-dict field on experiment id:%d (info-dict field '%s' not found) \n" % (entry["_id"], acc))




def main():
    parser = argparse.ArgumentParser(description='Retrieve and process results from sacred mongodb database')

    parser.add_argument('name',
                        metavar="name",
                        type=str,
                        help='List of experiments names',
                        nargs="+"
                        )


    parser.add_argument('--parameters',
                        metavar='parameters',
                        type=str,
                        nargs='+',
                        help='Config parameters to group by',
                        default=[]
                        )


    parser.add_argument('--accumulate',
                        type=str,
                        help='info-dict fields to accumulate (experiments results are accumulated by default)',
                        nargs="*",
                        default=[]
                        )

    parser.add_argument('--reduce',
                        choices=reducers.keys(),
                        help='Reducers to use on the accumulated data',
                        nargs="*",
                        default=[]
                        )


    parser.add_argument('--db',
                        type=str,
                        help='MongoDB database name',
                        default="sacred"
                        )


    parser.add_argument('--mongodb-uri',
                        type=str,
                        help='MongoDB uri to connect',
                        default=None
                        )

    parser.add_argument('--output',
                        choices=["table", "csv"],
                        help='Output format',
                        default="table"
                        )
    
    parser.add_argument('--missing',
                        type=str,
                        help='How to handle missing parameters values (use "drop" to drop or a value to overwrite)',
                        default="drop"
                        )
    
    
    for reducer in reducers:
        reducers[reducer].add_args(parser)

    args = parser.parse_args()

    use_reducers = dict()

    for reducer in args.reduce:
        use_reducers[reducer] = reducers[reducer](args)

    client = pymongo.MongoClient(args.mongodb_uri) 

    runs = client[args.db].runs

    hashmap = dict()
    for name in args.name:
        entries = runs.find({'experiment.name': name, "status": "COMPLETED"})
        accumulate_entries(hashmap, entries, args)

    accumulators = ["results"] + args.accumulate

    fields = []
    for accumulator in accumulators:
        for reducer in use_reducers:
            fields.append("%s (%s)" % (accumulator, use_reducers[reducer].name))


    field_names = args.parameters + fields
    rows = []
    for key in hashmap:
        row = key.split("_")
        row = [] if len(row) == 1 and row[0] == "" else row 
        for accumulator in accumulators:
            for reducer in use_reducers:
                row.append(use_reducers[reducer](hashmap[key][accumulator]))
        rows.append(row)

    if args.output == "table":
        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names = field_names
        for row in rows:
            table.add_row(row)
        print(table)
    elif args.output == "csv":
        print(",".join(field_names))
        for row in rows:
            print(",".join(row))

if __name__ == "__main__":
    main()