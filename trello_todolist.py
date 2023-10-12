import asyncio
from tasks.get_task import get_trello_tasks
from tasks.add_task import add_task_todoist

async def main():
    tasks = await get_trello_tasks()
    await add_task_todoist(tasks)

    print("Tareas agregadas a Todoist.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())