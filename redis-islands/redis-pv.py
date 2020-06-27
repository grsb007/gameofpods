#!/usr/bin/env python3
# TODO: Figure out some yaml templating system like jinja or ksonnet or
# whatever that doesn't make me want to claw my eyeballs out

template = """---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis0{num}
  labels:
    type: local
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: manual
  capacity:
    storage: 1Gi
  hostPath:
    path: /redis0{num}"""

for i in range(1, 6):
    with open(f'./redis-pv-0{i}.yaml', 'w') as f:
        f.write(template.format(num=i))

