# chat-server
A very simple python TCP chat server. This was created to apply the pushing model


# How to run it?
* Install python in your machine
* Install Python libraries using `pip install requirements.txt`
* Run the program by using `python main.py`
* Use `localhost:5555` to connect using javascript in your browser console by typing the following:

```js
const ws = new WebSocket('ws://localhost:5555');
ws.onmessage = message => (console.log(message.data))
```

* To send a message use the following

```js
ws.send("hello world")
```

* Connect multiple clients and start chat with yourself :)
