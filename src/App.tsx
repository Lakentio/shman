import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import ScriptList from './components/ScriptList';
import ScriptEditor from './components/ScriptEditor';
import ScriptVersions from './components/ScriptVersions';
import ScriptLogs from './components/ScriptLogs';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <Navbar />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<ScriptList />} />
            <Route path="/edit/:name" element={<ScriptEditor />} />
            <Route path="/versions/:name" element={<ScriptVersions />} />
            <Route path="/logs/:name" element={<ScriptLogs />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;