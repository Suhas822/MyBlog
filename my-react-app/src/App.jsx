import React, { useState } from 'react';

const AutocompleteChips = () => {
  const [items] = useState(['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']);
  const [inputValue, setInputValue] = useState('');
  const [selectedChips, setSelectedChips] = useState([]);

  const filterItems = () => {
    return items.filter(item => !selectedChips.includes(item) && item.toLowerCase().includes(inputValue.toLowerCase()));
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleItemClick = (item) => {
    setSelectedChips([...selectedChips, item]);
    setInputValue(''); // Clear the input value after selecting an item
  };

  const handleChipRemove = (chip) => {
    setSelectedChips(selectedChips.filter(item => item !== chip));
  };

  return (
    <div style={{ maxWidth: '300px', marginBottom: '200px', padding: '20px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '8px' }}>
      <div style={{ display: 'flex', flexWrap: 'wrap', marginBottom: '10px' }}>
        {selectedChips.map(chip => (
          <div
            key={chip}
            style={{ backgroundColor: '#3498db', color: '#fff', padding: '8px 12px', borderRadius: '20px', marginRight: '8px', marginBottom: '8px', fontSize: '14px' }}
          >
            {chip}
            <span
              onClick={() => handleChipRemove(chip)}
              style={{ cursor: 'pointer', fontSize: '16px', marginLeft: '4px' }}
            >
              X
            </span>
          </div>
        ))}
      </div>
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        placeholder="Search..."
        style={{ width: '100%', padding: '10px', border: '1px solid #ddd', borderRadius: '4px', fontSize: '16px' }}
      />
      <ul style={{ width: '200px', listStyle: 'none', padding: '0', margin: '0' }}>
        {filterItems().map(item => (
          <li
            key={item}
            onClick={() => handleItemClick(item)}
            style={{ cursor: 'pointer', padding: '10px', backgroundColor: '#f2f2f2', borderRadius: '4px', marginBottom: '5px', transition: 'background-color 0.3s' }}
          >
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <AutocompleteChips />
    </div>
  );
}

export default App;
