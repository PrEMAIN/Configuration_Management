import argparse
from src.visualizer import visualize_graph

def main():
    parser = argparse.ArgumentParser(description="Visualize git commit dependencies.")
    parser.add_argument('--config', type=str, help="Path to the config file", required=True)
    args = parser.parse_args()
    
    visualize_graph(args.config)

if __name__ == "__main__":
    main()
