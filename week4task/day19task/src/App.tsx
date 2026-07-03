import "./App.css";

import Counter from "./components/Counter";
import Card from "./components/Card";
import List from "./components/List";

function App() {
  return (
    <div className="container">
      <h1>React Fundamentals</h1>

      <Counter />

      <hr />

      <h2>Reusable Cards</h2>

      <Card
        title="React"
        description="React is a JavaScript library used to build user interfaces."
      />

      <Card
        title="TypeScript"
        description="TypeScript adds static typing to JavaScript."
      />

      <Card
        title="Vite"
        description="Vite is a fast frontend build tool."
      />

      <hr />

      <List />
    </div>
  );
}

export default App;