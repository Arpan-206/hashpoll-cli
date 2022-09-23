# Hashpoll (CLI)

![Hashpoll Banner](assets/Hashpoll.png)

Hashpoll is a hashnode widget that enables seamless polls on any post. It is a lightweight tool that generates code for you to put in hashnode's widget field to create polls that just blend in with the rest of your content. You can use it directly from the command line or through the Web interface, and manage your poll as needed.

Hashpoll CLI is a handy tool to extend and supplement Hashpoll. It allows you to seamlessly create polls from the command line. The tool automatically gives you the code to place in the widgets section of Hashnode. 

## Installation

Install hashpoll-cli with pip

```bash
  pip install hashpoll-cli
```
    
# Hashnode Widgets

You can learn how to use hashnode widget over [here](https://townhall.hashnode.com/hashnode-widgets).
## Commands

### Create
This is the command to create polls from the CLI.  

```bash
hashpoll create [question] --option1 [option1] --option2 [option2] --option3 [option3] --option4 [option4]
```
or
```bash
python -m hashpoll create [question] --option1 [option1] --option2 [option2] --option3 [option3] --option4 [option4]
```

[![asciicast](https://asciinema.org/a/pZfU2ZIyot72RmtSD6yzfSioz.svg)](https://asciinema.org/a/pZfU2ZIyot72RmtSD6yzfSioz)

#### Tips
1. Put the question or options (if multiple words) in quotes to avoid the terminal registering this as multiple arguments.
2. If you miss adding one of the options, the program will prompt you for entering them.

### View
This is a command for viewing all details of a particular poll.

```bash
hashpoll view [Poll ID]
```

or 

```bash
python -m hashpoll view [Poll ID]
```

[![asciicast](https://asciinema.org/a/LHrMNStGjVkRMP4hbGu5otF0L.svg)](https://asciinema.org/a/LHrMNStGjVkRMP4hbGu5otF0L)

### Vote
This is a command to vote on a specific poll.

```bash
hashpoll vote [Poll ID] [Option Number]
```

or

```bash
python -m hashpoll vote [Poll ID] [Option Number]
```

[![asciicast](https://asciinema.org/a/1FDpi9gaVHZqeaLuxKAnjXecg.svg)](https://asciinema.org/a/1FDpi9gaVHZqeaLuxKAnjXecg)

### Open-poll
This is a simple command to open a poll in the default browser.

```bash
hashpoll open-poll [Poll ID]
```

or

```bash
python -m hashpoll open-poll [Poll ID]
```

[![asciicast](https://asciinema.org/a/wA9D9Smrwx3H1dVkiaXZ1FzWC.svg)](https://asciinema.org/a/wA9D9Smrwx3H1dVkiaXZ1FzWC)

### Results
This is a command to fetch the current data from poll responses.

```bash
hashpoll results [Poll ID]
```

or

```bash
python -m hashpoll results [Poll ID]
```

[![asciicast](https://asciinema.org/a/p455OvYTuy6e7Q9bECDWWDkbT.svg)](https://asciinema.org/a/p455OvYTuy6e7Q9bECDWWDkbT)

### Code
This is handy commad to generate the Hashnode Widget Code for a particular poll.

```bash
hashpoll code [Poll ID]
```

or 

```bash
python -m hashpoll code [Poll ID]
```

[![asciicast](https://asciinema.org/a/0R0xeOpRnSphSxKHOvVNcq2uR.svg)](https://asciinema.org/a/0R0xeOpRnSphSxKHOvVNcq2uR)
## Features

- Lightweight
- CLI and Web Based
- Seamless
- Easy-to-integrate


## Authors

- [@Arpan-206](https://github.com/Arpan-206)


## Tech Stack

**Client:** AWS Amplify, Svelte, Typer, Rich, PicoCSS

**Server:** Node, AWS Amplify, FastAPI

## Roadmap

- Password Protection

- In-depth analytics

- Authentication

- Ability to modify a poll


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

Hashpoll would like to thank the teams behind the following projects as they played a crucial part in enabling Hahpoll.

 - [AWS Amplify](https://aws.amazon.com/amplify/)
 - [Hashnode](https://hashnode.com/)
 - [FastAPI](https://fastapi.tiangolo.com/)
 - [Typer](https://typer.tiangolo.com/)
 - [PicoCSS](https://picocss.com/)


## Feedback

If you have any feedback, please reach out to us at [arpan@hackersreboot.tech](mailto:arpan@hackersreboot.tech).


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.