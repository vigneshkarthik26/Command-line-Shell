import os
import sys
import shlex
import subprocess

def execute_comm(comm_tkns):
    if not comm_tkns:
        return
    
    cmd = comm_tkns[0]

    if cmd == 'cd':
        try:
            target_path = comm_tkns[1] if len(comm_tkns)>1 else os.path.expanduser("~")
            os.chdir(target_path)
        except FileNotFoundError:
            print(f"cd: no such file or directory: {target_path}")
    
    elif cmd == 'exit':
        print("Exiting shell")
        sys.exit(0)
    
    else:
        try:
            subprocess.run(comm_tkns)
        except FileNotFoundError:
            print(f"{cmd}: Command not found")
        except Exception as e:
            print(f"Error: {e}")

def main():
    while True:
        try:
            cwd = os.getcwd()
            comm_ip = input(f"{cwd} $ ")
            comm_tkns = shlex.split(comm_ip)
            execute_comm(comm_tkns)
        except EOFError:
            print("\nExit")
            break
        except KeyboardInterrupt:
            print()

if __name__ == "__main__":
    main()