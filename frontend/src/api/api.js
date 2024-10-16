export const getExpenses = async () => {
    return [
      { description: 'Groceries', amount: 50, category: 'Groceries' },
      { description: 'Rent', amount: 1000, category: 'Rent' },
      { description: 'Movie', amount: 30, category: 'Entertainment' },
    ];
  };
  
  export const uploadStatement = async (file) => {
    console.log("File uploaded:", file.name);
  };
  