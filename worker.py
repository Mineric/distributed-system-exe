import multiprocessing

def worker(num):
    """Task to be performed by each worker process"""
    print(f'Worker {num} processing task')

if __name__ == '__main__':
    # Create a list of worker processes
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    
    # Wait for all worker processes to complete
    for p in processes:
        p.join()
