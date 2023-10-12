import asyncio
from pyppeteer import launch

async def login_todoist():
  print("Iniciando sesión en Todoist...")
  
  user = "testingoli26@gmail.com"
  password = "Pepepecas1"
  
  browser = await launch()
  page = await browser.newPage()

  await page.goto("https://todoist.com/auth/login")
  
  # Revisa los selectores que contiene la página
  selectores = await page.evaluate('() => { return Array.from(document.querySelectorAll("*"), element => element.tagName + (element.id ? "#" + element.id : "") + (element.className ? "." + element.className : "")) }')
  print(selectores)

  await page.waitForSelector("A")
  await page.waitForSelector("P")

  await page.type("A", user)
  await page.type("P", password)

  await page.click("DIV#todoist_app")
  
  print("Agregando tareas a Todoist...")
  await page.waitForSelector(".task_list")

  await browser.close()

async def add_task_todoist(tasks):
  await login_todoist()

  browser = await launch()
  page = await browser.newPage()

  await page.goto("https://todoist.com/app")

  await page.waitForSelector(".quick_add")

  for task in tasks:
      await page.type(".quick_add", task)
      await page.keyboard.press("Enter")
      await page.waitForSelector(".task_list")

  await browser.close()
