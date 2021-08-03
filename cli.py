# pylint: disable=import-outside-toplevel
import click


@click.group()
def cli():
    """App commands"""


@cli.command()
def run():
    from engine import Engine

    click.echo("Running...")
    engine = Engine()
    engine.loop()


@cli.command()
def asearch():
    from maze_gen import MazeGen
    from a_search import AStarSearch

    maze = MazeGen(10, 10).generate()
    click.echo(maze)
    search = AStarSearch(maze, (0, 0), (9, 9))
    #  print(search.neighbors((0, 0)))
    came_from, _ = search.run()
    path = search.reconstruct_path(came_from)
    print(path)


if __name__ == "__main__":
    cli()
