import { useParams } from 'react-router-dom';

interface Version {
  version: string;
  timestamp: string;
  message: string;
}

function ScriptVersions() {
  const { name } = useParams<{ name: string }>();
  // TODO: Fetch actual versions from the backend
  const versions: Version[] = [];

  return (
    <div className="bg-white shadow rounded-lg">
      <div className="px-4 py-5 sm:px-6">
        <h2 className="text-lg font-medium text-gray-900">Versions: {name}</h2>
      </div>
      <ul className="divide-y divide-gray-200">
        {versions.map((version) => (
          <li key={version.version} className="px-4 py-4">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-lg font-medium text-gray-900">Version {version.version}</h3>
                <p className="text-sm text-gray-500">{new Date(version.timestamp).toLocaleString()}</p>
                <p className="text-sm text-gray-700 mt-1">{version.message}</p>
              </div>
              <button
                onClick={() => {/* TODO: Implement restore functionality */}}
                className="inline-flex items-center px-3 py-2 border border-gray-300 text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
              >
                Restore
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ScriptVersions;