import json
from flask import Flask
from op_stats.stats import Stats

app=Flask(__name__)
@app.route('/v1/stats/cpu')
def get_cpu_percent():
  cpu_percent=Stats.get_cpu_percent()
#  return {'cpu_percent':cpu_percent}
  return json.dumps({'cpu_percent':cpu_percent})

@app.route('/v1/stats/memory')
def get_memoryinfo():
    memory_info = Stats.get_available_memory()
    return json.dumps({'memoria_disponible(MB)': memory_info})

@app.route('/v1/stats/disk')
def get_diskinfo():
    disk_info = Stats.get_disk_space()
    return json.dumps({'espacio_en_disco(MB)': disk_info})

if __name__ =='__main__':
  app.run(host='0.0.0.0', port=8080)
