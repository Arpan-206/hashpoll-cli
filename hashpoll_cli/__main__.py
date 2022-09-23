import typer
from rich import print
from rich.progress import BarColumn, Progress
from rich.syntax import Syntax
from rich.table import Table

from hashpoll_cli.helpers.create import create_help
from hashpoll_cli.helpers.get_poll import get_poll_help
from hashpoll_cli.helpers.get_responses import get_responses_help
from hashpoll_cli.helpers.vote import vote_help

app = typer.Typer()

@app.callback()
def main():
    """A handy CLI tool for creating polls for Hashnode.\n Made with ❤️ by @hashpoll."""
    pass


@app.command()
def vote(poll_id: str, option: int):
    """Vote in a poll."""
    if option not in [1, 2, 3, 4]:
        raise ValueError("Option must be 1, 2, 3, 4")
    res = vote_help(poll_id, option)
    if res:
        print("[green]Vote successful!")
    else:
        print("[red]Vote failed! Maybe the Poll ID is wrong?")

def valid_callback(value: str):
    if len(value) > 30:
        raise typer.BadParameter("Values must be less than 30 characters")
    return value

@app.command()
def create(question: str, option1: str = typer.Option(..., "--option1", "-o1", prompt=True, callback=valid_callback), option2: str = typer.Option(..., "--option2", "-o2", prompt=True, callback=valid_callback), option3: str = typer.Option(..., "--option3", "-o3", prompt=True, callback=valid_callback), option4: str = typer.Option(..., "--option4", "-o4", prompt=True, callback=valid_callback)):
    """Create a poll."""
    my_url = "https://hashpoll.hackersreboot.tech/vote/"
    
    res = create_help(question, option1, option2, option3, option4)
    if res:
        res = res["poll"]
        print(f"[cyan]Created a poll with ID {res['id']}")
        print(f"[blue]The form is located over at: {my_url}{res['id']}")
        my_table = Table(show_header=True, header_style="bold orange1")
        my_table.add_column("Poll ID", style="dim", width=36)
        my_table.add_column("Question", style="dim", width=36)
        my_table.add_column("Option 1", style="dim", width=36)
        my_table.add_column("Option 2", style="dim", width=36)
        my_table.add_column("Option 3", style="dim", width=36)
        my_table.add_column("Option 4", style="dim", width=36)
        my_table.add_row(res["id"], res["question"], res["option1"],
                         res["option2"], res["option3"], res["option4"])
        print(my_table)
        print(f"[blue]The form is located over at: {my_url}{res['id']}")
        print("[blue]The hashnode code for the poll is:")
        print(Syntax(f"""<iframe src="{my_url}/{res['id']}" 
style="border:0px #ffffff none;" name="myiFrame" scrolling="yes" frameborder="0"
marginheight="0px" marginwidth="0px" height="150%" width="100%" allowfullscreen>
</iframe>""",
                    "html", theme="one-dark"))
        typer.launch(my_url + res["id"])
    else:
        print("[red]Poll creation failed!")


@app.command()
def open_poll(poll_id: str):
    """Open a poll in your browser."""
    my_url = "https://hashpoll.hackersreboot.tech/vote/"
    typer.launch(my_url + poll_id)


@app.command()
def view(poll_id: str):
    """View a poll."""
    res = get_poll_help(poll_id)
    if res:
        my_table = Table(show_header=True, header_style="bold blue")
        my_table.add_column("Poll ID", style="dim", width=36)
        my_table.add_column("Question", style="dim", width=36)
        my_table.add_column("Option 1", style="dim", width=36)
        my_table.add_column("Option 2", style="dim", width=36)
        my_table.add_column("Option 3", style="dim", width=36)
        my_table.add_column("Option 4", style="dim", width=36)
        my_table.add_row(res["id"], res["question"], res["option1"],
                         res["option2"], res["option3"], res["option4"])
        print(my_table)
    else:
        print("[red]Poll not found!")


@app.command()
def results(poll_id: str):
    """View the results of a poll."""
    res = get_responses_help(poll_id)
    print("[cyan]Getting results...")
    print(f"[cyan]Question: {res['question']}")
    progress = Progress("[progress.description]{task.description}",BarColumn(), "[progress.percentage]{task.percentage:>3.0f}%")
    if res:
        print(f"[blue]Results for poll with ID: {res['id']}")
        op1 = (res["option1"] / res["responses"]) * 100
        op2 = (res["option2"] / res["responses"]) * 100
        op3 = (res["option3"] / res["responses"]) * 100
        op4 = (res["option4"] / res["responses"]) * 100
        with progress:
            option1 = progress.add_task("Option1", total=100)
            option2 = progress.add_task("Option2", total=100)
            option3 = progress.add_task("Option3", total=100)
            option4 = progress.add_task("Option4", total=100)

            progress.update(option1, completed=op1)
            progress.update(option2, completed=op2)
            progress.update(option3, completed=op3)
            progress.update(option4, completed=op4)
            

    else:
        print("[red]Poll not found!")

@app.command()
def code(poll_id: str, save: bool = typer.Option(False, "--save", "-s")):
    """Get the code for a poll."""
    res = get_poll_help(poll_id)
    if not res:
        print("[red]Poll not found!")
        return
    my_url = "https://hashpoll.hackersreboot.tech/vote/"
    print("[blue]The hashnode code for the poll is:")
    print(Syntax(f"""<iframe src="{my_url}/{poll_id}" 
style="border:0px #ffffff none;" name="myiFrame" scrolling="yes" frameborder="0"
marginheight="0px" marginwidth="0px" height="150%" width="100%" allowfullscreen>
</iframe>""",
                    "html", theme="one-dark"))
    if save:
        with open("poll_code.html", "w") as f:
            f.write(f"""<iframe src="{my_url}/{poll_id}" 
style="border:0px #ffffff none;" name="myiFrame" scrolling="yes" frameborder="0"
marginheight="0px" marginwidth="0px" height="150%" width="100%" allowfullscreen>
</iframe>""")
        print("[blue]Saved code to poll_code.html")

if __name__ == "__main__":
    app()
