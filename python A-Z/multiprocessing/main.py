# main.py created inside day 98
# Multiprocessing involves using multiple CPUs to run many processes at a time, while multithreading creates multiple threads within a single process to achieve faster and more efficient task execution.

#98. multiprocessing
import requests
import multiprocessing
import concurrent.futures

url= "https://picsum.photos/2000/3000"
def downloadfile(url,name):
    print(f"started downloading file {name}")
    response=requests.get(url)
    open(f"multiprocessing/file{name}.jpg", "wb").write(response.content)
    print(f"finished downloading {name}")
#1st method
for i in range(5):
    downloadfile(url,i)

#2nd method
pros = []
for i in range(5):
# downloadFile(url, i)
    p = multiprocessing.Process(target=downloadfile, args=[url, i])
    p.start()
    pros.append(p)
    
for p in pros:
    p.join()
    
#3rd method
with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(60)]
    l2 = [i for i in range(60)]
    results = executor.map(downloadfile, l1, l2)
    for r in results:
        print(r)
        
