from data_loader import harmonize_series, response
from preprocessing import harmonize_series, response
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Training config')
    parser.add_argument('--data', type=str, default='harmonize_series',help='')
    parser.add_argument('--batch_size', type=int, default=4,help='')
    parser.add_argument('--epoch', type=int, default=100,help='')
    parser.add_argument('--batch_size', type=int, default=4,help='')
