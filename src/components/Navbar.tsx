import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="bg-indigo-600">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="text-white font-bold text-xl">
            ShMan
          </Link>
          <div className="flex space-x-4">
            <Link to="/" className="text-white hover:text-indigo-200">
              Scripts
            </Link>
            <button
              onClick={() => {/* TODO: Implement new script modal */}}
              className="bg-white text-indigo-600 px-4 py-2 rounded-md hover:bg-indigo-100"
            >
              New Script
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;