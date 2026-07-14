import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { App } from './App';

describe('App', () => {
  it('renders paper banner and disconnected state', () => {
    render(<App />);
    expect(screen.getByRole('heading', { name: /MODO PAPER TRADING/i })).toBeInTheDocument();
    expect(screen.getByText(/Backend sin conectar/i)).toBeInTheDocument();
  });
});
