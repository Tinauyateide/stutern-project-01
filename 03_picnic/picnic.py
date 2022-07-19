#!/usr/bin/env python3
"""Picnic game"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='item(s) to bring')



    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='sort the items'),
                        

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num_items = len(items)

    if args.sorted:
        items.sort()

    bringing  = ''
    if num_items == 1:
        bringing = items[0]
    elif num_items == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)
        
    

    print(f'You are bringing {bringing}.')




# -------------------------------------------------- 
if __name__ == '__main__':
    main()
