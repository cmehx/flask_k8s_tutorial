""" A very long statement that just goes on and on and on and on and
  never ends until after it's reached the 80 char limit
"""
import os
from flask import Flask
from redis import Redis

redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'),
              port=os.getenv('REDIS_PORT', '6379'))
app = Flask(__name__)

@app.route('/')
# A very long statement that just goes on and on and on and on and
# never ends until after it's reached the 80 char limit
def hello():
    """ azeazeazeaze
  azeazeaze
    """
    redis.incr('hits')
    hits = int(redis.get('hits'))
    return f"Hits: {hits}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
