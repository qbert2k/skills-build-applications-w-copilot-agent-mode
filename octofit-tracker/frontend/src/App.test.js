import { render, screen } from '@testing-library/react';
import App from './App';

test('renders OctoFit Tracker navbar', () => {
  render(<App />);
  const navbarBrand = screen.getByText(/OctoFit Tracker/i);
  expect(navbarBrand).toBeInTheDocument();
});
