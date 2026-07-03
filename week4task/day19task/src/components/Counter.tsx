import { useState } from "react"; //normal variable cannot update the UI when its value changes.

function Counter() { //functional com
  const [count, setCount] = useState<number>(0);

  return (
    <div className="counter">
      <h2>Counter Component</h2>

      <h1>{count}</h1>

      <button onClick={() => setCount(count + 1)}>
        Increment +
      </button>

      <button onClick={() => setCount(count - 1)}>
        Decrement -
      </button>

      <button onClick={() => setCount(0)}>
        Reset 0
      </button>
    </div>
  );
}

export default Counter;