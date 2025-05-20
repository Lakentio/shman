import { useParams } from 'react-router-dom';

interface Log {
  id: string;
  timestamp: string;
  content: string;
}

function ScriptLogs() {
  const { name } = useParams<{ name: string }>();
  // TODO: Fetch actual logs from the backend
  const logs: Log[] = [];

  return (
    <div className="bg-white shadow rounded-lg">
      <div className="px-4 py-5 sm:px-6">
        <h2 className="text-lg font-medium text-gray-900">Execution Logs: {name}</h2>
      </div>
      <ul className="divide-y divide-gray-200">
        {logs.map((log) => (
          <li key={log.id} className="px-4 py-4">
            <div>
              <h3 className="text-sm font-medium text-gray-900">
                {new Date(log.timestamp).toLocaleString()}
              </h3>
              <pre className="mt-2 text-sm text-gray-700 whitespace-pre-wrap">
                {log.content}
              </pre>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ScriptLogs;