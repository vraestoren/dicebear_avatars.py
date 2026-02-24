from os import getcwd
from time import time
from pathlib import Path
from requests import Session

class DiceBearAvatars:
	def __init__(self) -> None:
		self.api = "https://avatars.dicebear.com/api"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}
	
	def save_file(
			self,
			format: str,
			content: bytes,
			location: str = getcwd()) -> bool:
		with open(
			Path(location).joinpath(f"{time() * 1000}.{format}"), mode="wb+") as file:
				file.write(content)
				file.close()
		return True

	def get_avatar(
			self,
			sprite: str,
			seed: str,
			background: str = None,
			mood: str = "happy",
			format: str = "svg") -> bool:
		url = f"{self.api}/{sprite}/{seed}.{format}?mood[]={mood}"
		if background:
			url += f"&background={background}"
		return self.save_file(format, self.session.get(url).content)
