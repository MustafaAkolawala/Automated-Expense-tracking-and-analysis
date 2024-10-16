import React, { useState } from 'react';
import { uploadStatement } from '../api/api';

const UploadStatement = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (file) {
      await uploadStatement(file);
      alert("File uploaded successfully");
    } else {
      alert("Please select a file first");
    }
  }

  return (
    <div>
      <h2>Upload Bank Statement</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default UploadStatement;
