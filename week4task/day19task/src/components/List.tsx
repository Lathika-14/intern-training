function List() {
  const fruits = [
    " Apple",
    " Banana",
    " Orange",
    " Mango",
    " kiwi",
  ];

  return (
    <div className="list">
      <h2> Fruit List</h2>

      <ul>
        {fruits.map((fruit, index) => (
          <li
            key={index}
            className={fruit.length > 8 ? "highlight" : ""}
          >
            {fruit}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default List;