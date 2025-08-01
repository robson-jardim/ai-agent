
import React, { useState } from 'react';
import { Link, Outlet } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { AppBar, Toolbar, IconButton, Typography, Select, MenuItem, CssBaseline, Drawer, List, ListItem, ListItemText, createTheme, ThemeProvider } from '@mui/material';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';

export default function DashboardLayout() {
  const { t, i18n } = useTranslation();
  const [darkMode, setDarkMode] = useState(false);
  const theme = createTheme({ palette: { mode: darkMode ? 'dark' : 'light' } });

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <div style={{ display: 'flex' }}>
        <Drawer variant="permanent" anchor="left">
          <Toolbar />
          <List>
            <ListItem button component={Link} to="/">
              <ListItemText primary={t('dashboard')} />
            </ListItem>
            <ListItem button component={Link} to="/settings">
              <ListItemText primary={t('settings')} />
            </ListItem>
          </List>
        </Drawer>
        <div style={{ flexGrow: 1 }}>
          <AppBar position="static">
            <Toolbar style={{ justifyContent: 'space-between' }}>
              <Typography variant="h6">{t('dashboard')}</Typography>
              <div>
                <IconButton onClick={() => setDarkMode(!darkMode)} color="inherit">
                  {darkMode ? <Brightness7Icon /> : <Brightness4Icon />}
                </IconButton>
                <Select
                  value={i18n.language}
                  onChange={(e) => i18n.changeLanguage(e.target.value)}
                  style={{ color: '#fff', marginLeft: '1rem' }}
                >
                  <MenuItem value="en">EN</MenuItem>
                  <MenuItem value="pt">PT</MenuItem>
                </Select>
              </div>
            </Toolbar>
          </AppBar>
          <main style={{ padding: '1rem' }}>
            <Outlet />
          </main>
        </div>
      </div>
    </ThemeProvider>
  );
}
