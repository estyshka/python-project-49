install: #установка и обновление зависимостей
	uv sync

brain-games: #запуск программы
	uv run brain-games

build: #собираем пакет -- директория /dist
	uv build
package-install: #установка пакета в операционную систему
	uv tool install dist/*.whl

lint: #запустить проверку линтером
	uv run ruff check brain_games

bri:
	uv run brain-even