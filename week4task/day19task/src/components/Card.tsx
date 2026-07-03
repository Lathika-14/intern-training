type CardProps = {
  title: string;
  description: string;
};

function Card({ title, description }: CardProps) { //func comp
  return (
    <div className="card">
      <div>
        <h2>{title}</h2>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default Card;