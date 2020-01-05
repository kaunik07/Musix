import argparse
from downloader import * 

def title():
    print("*------------------------------------------------*")
    print("/ |\    /| |   |  |''''  '''|'''   \\  //        /")
    print("/ | \  / | |   |  |         |       \\//         /")
    print("/ |  \/  | |   |  |''''|    |       //\\         /")
    print("/ |      | |___|   ,,,,| ,,,|,,,   //  \\        /")
    print("*------------------------------------------------*")

def version():
    print("v1.0")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s","--song",action="store_true",help="search for songs")
    group.add_argument("-v","--version",action="store_true",help="version")
    args = parser.parse_args()

    if args.song:
        title()
        downloadSong()
    
    if args.version:
        version()


    