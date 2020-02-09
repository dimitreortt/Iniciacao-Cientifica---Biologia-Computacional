import subprocess as sp

sp.call(['mpiexec', '-n', '4', 'python','modeOne_paralelo.py', 'input1'])