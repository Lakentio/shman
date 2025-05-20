import { Link } from 'react-router-dom';

interface Script {
  name: string;
  category: string;
  tags: string[];
  created_at: string;
}

function ScriptList() {
  // TODO: Fetch actual scripts from the backend
  const scripts: Script[] = [
    {
      name: "backup",
      category: "system",
      tags: ["backup", "automation"],
      created_at: "2024-01-01T00:00:00Z"
    }
  ];

  return (
    <div className="bg-white shadow rounded-lg">
      <div className="px-4 py-5 sm:px-6">
        <h2 className="text-lg font-medium text-gray-900">Your Scripts</h2>
      </div>
      <ul className="divide-y divide-gray-200">
        {scripts.map((script) => (
          <li key={script.name} className="px-4 py-4">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-lg font-medium text-gray-900">{script.name}</h3>
                <p className="text-sm text-gray-500">{script.category}</p>
                <div className="mt-1 flex space-x-2">
                  {script.tags.map((tag) => (
                    <span
                      key={tag}
                      className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-indigo-100 text-indigo-800"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
              <div className="flex space-x-2">
                <Link
                  to={`/edit/${script.name}`}
                  className="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
                >
                  Edit
                </Link>
                <Link
                  to={`/versions/${script.name}`}
                  className="inline-flex items-center px-3 py-2 border border-gray-300 text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                >
                  Versions
                </Link>
                <Link
                  to={`/logs/${script.name}`}
                  className="inline-flex items-center px-3 py-2 border border-gray-300 text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                >
                  Logs
                </Link>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ScriptList;