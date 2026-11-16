"""Replay the complete published extensions to both global cost lower bounds."""
import json
from replay import verify

if __name__ == "__main__":
    print(json.dumps(verify({11:10961,12:9824}),indent=2,sort_keys=True))
