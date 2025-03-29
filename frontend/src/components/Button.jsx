const Button = ({ onClick }) => {
  return (
    <button
      className="mt-4 px-6 py-3 bg-green-800 text-white rounded-full font-semibold shadow-lg hover:bg-green-700 hover:scale-105 transition-all duration-300"
      onClick={onClick}
    >
      🔍 Check Spam
    </button>
  );
};

export default Button;
