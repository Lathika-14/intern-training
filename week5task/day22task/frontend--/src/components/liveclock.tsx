import { useEffect, useState } from "react";
//This creates a React component.It can be used like <LiveClock />
export default function LiveClock() {
  const [time, setTime] = useState("");

  useEffect(() => {
    const eventSource = new EventSource(
      `${import.meta.env.VITE_API_URL}/events`
    );
//EventSource is a browser API used for Server-Sent Events (SSE).Its job is to create a connection with the server that stays open.
    eventSource.onmessage = (event) => {
      setTime(event.data);
    };
//This function runs every time the server sends new data.

    eventSource.onerror = () => {
      console.log("Connection error");
      eventSource.close();
    };
//api closing
//connection closing
    return () => {
      eventSource.close();
    };
  }, []);
  //The empty array [] means this effect runs only once when the component mounts.

  return (
    <div>
      <h2>Live Time</h2>
      <h1>{time}</h1>
    </div>
  );
}