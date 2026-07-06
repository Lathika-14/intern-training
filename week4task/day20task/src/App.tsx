import { useState, useEffect } from "react";

interface Student {
  name: string;
  email: string;
}

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [students, setStudents] = useState<Student[]>([]); //Array of Student objects.

  useEffect(() => { //Runs only once.
    console.log("Student Form Loaded");
  }, []); //Empty dependency array.

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); //prevent the default form submission behavior
    //it contains everything about submit event --e parameter


    if (name.trim() === "" || email.trim() === "") {
      alert("Please fill all the fields.");
      return;
    }

    const newStudent: Student = {
      name,
      email,
    };

    setStudents([...students, newStudent]); //using spread operator to add new student and create new array

    setName(""); //after submission the input field should be empty
    setEmail("");
  };

  return ( 
    <div className="min-h-screen bg-gray-100 flex justify-center items-center p-6">
      <div className="bg-white shadow-lg rounded-xl p-8 w-full max-w-md"> 
        <h1 className="text-3xl font-bold text-center text-blue-600 mb-6"> 
          Student Form
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4"> 
          <div>
            <label className="block mb-2 font-semibold">
              Name
            </label>

            <input
              type="text"
              placeholder="Enter your name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label className="block mb-2 font-semibold"> 
              Email
            </label>

            <input
              type="email"
              placeholder="Enter your email"
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
              className="w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700"
          >
            Add Student
          </button>

        </form>

        <h2 className="text-2xl font-bold text-green-600 mt-8 mb-4"> 
          Student List
        </h2>

        {students.length === 0 ? (
          <p className="text-gray-500">No students added yet.</p>
        ) : (
          <div className="space-y-3">
            {students.map((student, index) => (
              <div
                key={index}
                className="border rounded-lg p-4 shadow bg-gray-50"
              >
                <p>
                  <strong>Name:</strong> {student.name}
                </p>

                <p>
                  <strong>Email:</strong> {student.email}
                </p>
              </div>
            ))}
          </div>
        )}

      </div>
    </div>
  );
}

export default App;