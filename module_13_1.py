import asyncio

async def start_strongman(name, power):
    print(f"На помост приглашается силач {name}!")
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i+1}-й шар")
    print(f"Силач {name} закончил упражнение")

async def start_tournament():
    print("Приветствуем участников соревнований!")
    sil_1 = asyncio.create_task(start_strongman('Pasha', 3))
    sil_2 = asyncio.create_task(start_strongman('Denis', 4))
    sil_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await sil_1
    await sil_2
    await sil_3
    print("Соревнования закончены!")

asyncio.run(start_tournament())