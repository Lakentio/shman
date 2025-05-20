import { useParams } from 'react-router-dom';
import { useState } from 'react';
import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import bash from 'react-syntax-highlighter/dist/esm/languages/hljs/bash';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';

SyntaxHighlighter.registerLanguage('bash', bash);

function ScriptEditor() {
  const { name } = useParams<{ name: string }>();
  const [content, setContent] = useState('#!/bin/bash\n\n# Your script here');

  const handleSave = () => {
    // TODO: Implement save functionality
    console.log('Saving script:', name, content);
  };

  return (
    <div className="bg-white shadow rounded-lg p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-lg font-medium text-gray-900">Editing: {name}</h2>
        <button
          onClick={handleSave}
          className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
        >
          Save Changes
        </button>
      </div>
      <div className="relative">
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
          className="w-full h-96 font-mono text-sm p-4 border rounded-md"
        />
        <div className="absolute inset-0 pointer-events-none">
          <SyntaxHighlighter
            language="bash"
            style={docco}
            className="h-full"
          >
            {content}
          </SyntaxHighlighter>
        </div>
      </div>
    </div>
  );
}

export default ScriptEditor;