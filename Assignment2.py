from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"Process {rank} of {size} started")

if rank == 0:
    # MASTER PROCESS
    print("\nMaster process running...\n")

    for i in range(1, size):
        message = comm.recv(source=i)
        print(f"Received from process {i}:")
        print(f"  Task: {message['task']}")
        print(f"  Result: {message['result']}\n")

else:
    # WORKER PROCESS
    data_chunk = list(range(rank * 10, rank * 10 + 10))
    result = sum(data_chunk)

    message = {
        "rank": rank,
        "task": f"Sum of numbers {data_chunk[0]} to {data_chunk[-1]}",
        "result": result
    }

    comm.send(message, dest=0)
