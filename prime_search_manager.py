from subprocess import run, Popen, PIPE, STDOUT
import time

# A large prime number
# big_prime = 22801763489

# A challenging composite with two large prime factors
big_prime = 299993 * 300007

# A *very* challenging composite with even larger prime factors
# big_prime = 1000000007 * 5000000029

max_concurrent_processes = 1

if __name__ == "__main__":
    if max_concurrent_processes < 1:
        raise ValueError("We can't have that, now can we O_o")
    
    result = 0
    
    if big_prime < 1000000000:
        # No point in dividing into smaller units than 5000
        result = run(f"python prime_search_worker.py {2} {big_prime - 1} {big_prime}".split()).returncode
    else:
        step = (big_prime // 2) // max_concurrent_processes
        cursor = 2
        
        plist: list[Popen] = []
        
        for i in range(max_concurrent_processes):
            plist.append(Popen(f"python prime_search_worker.py {cursor} {cursor + step} {big_prime}".split()))
            cursor += step
        
        while len(plist):
            done = filter(lambda p: p.poll() is not None, plist)
            
            for p in done:
                print("Got Done:", p.returncode)
                if p.returncode == 1:
                    result = 1
                
                plist.remove(p)
            
            if result == 1:
                break
            
            # Try not to hammer the CPU with too much unnecessary looping
            time.sleep(0.01)
                
        for p in plist:
            # Politely kill the children
            p.terminate()
        
    print("NOT PRIME!!" if result else "PRIME!!")
