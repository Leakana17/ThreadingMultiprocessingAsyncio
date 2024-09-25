import asyncio

async def async_write_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(str(line)+'\n')

async def run_async_tasks(primes):
    filename = [1,2,3,4,5,6,7,8,9,10]

    dataClean = [primes[i::10] for i in range(10)]

    
    tasks = [async_write_to_file(str(str(filename[i])+'.txt'), dataClean[i]) for i in range(10) ]

    # # Await the completion of all write tasks
    await asyncio.gather(*tasks)


