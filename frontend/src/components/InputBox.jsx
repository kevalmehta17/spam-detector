const InputBox = ({ text, setText }) => {
  return (
    <textarea
      className="w-80 h-32 p-3 border-none rounded-lg shadow-lg bg-white/80 text-gray-800 placeholder-gray-500 focus:outline-none focus:ring-4 focus:ring-green-300"
      placeholder="Enter text here..."
      value={text}
      onChange={(e) => setText(e.target.value)}
    />
  );
};

export default InputBox;
