import aiohttp
import asyncio
import os


async def download_image(url, session, save_path):
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.read()
            code = hash(response.url)
            filename = os.path.join(save_path, f"{code}.jpg")
            while os.path.exists(filename):
                code += 1
                filename = os.path.join(save_path, f"{code}.jpg")
            with open(filename, 'wb') as f:
                f.write(content)
            print(f"Downloaded: {filename}")


async def download_images(width, height, num_images, save_path):
    url = f"https://picsum.photos/{width}/{height}"
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(url, session, save_path) for _ in range(num_images)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    width = int(input("Input image width: "))
    height = int(input("Input image height: "))
    images_to_download = int(input("Input nums to download: "))
    save_directory = input("Input save directory: ")
    os.makedirs(save_directory, exist_ok=True)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_images(width, height, images_to_download, save_directory))
