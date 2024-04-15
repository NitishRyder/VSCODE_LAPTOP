import React from 'react';
import './form.css';

function Form() {
  return (
    <div className="form-container">
      <form className="form">
        <label htmlFor="name">Name:</label>
        <input type="text" id="name" name="name" />

        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" />

        <label htmlFor="password">Password:</label>
        <input type="password" id="password" name="password" />

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Form;