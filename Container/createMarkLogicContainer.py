import os
import subprocess

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# subprocess.run(
#         [
#             'docker',
#             'login',
#             '--username', '****',
#             '--password', '****'
#         ]
#     )
subprocess.run(
        [
            'docker',
            'run',
            '-it',
            '-d',
            '-p', '8000:8000',
            '-p', '8001:8001',
            '-p', '8002:8002',
            '-p', '8003:8003',
            '-p', '8004:8004',
            '-e', 'MARKLOGIC_INIT=true',
            '-e','MARKLOGIC_ADMIN_USERNAME=admin', '-e', 'MARKLOGIC_ADMIN_PASSWORD=admin',
            '--name', 'graphQlMarkLogic',
            'store/marklogicdb/marklogic-server:10.0-8.1-centos-1.0.0-ea2'
        ]
    )
