
import React from 'react';
import { useTranslation } from 'react-i18next';

export default function Login() {
  const { t } = useTranslation();
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '10%' }}>
      <h2>{t('login')}</h2>
      <button style={{ margin: '0.5rem' }}>Login with Google</button>
      <button style={{ margin: '0.5rem' }}>Login with Apple</button>
      <button style={{ margin: '0.5rem' }}>Login with Mobile Number</button>
    </div>
  );
}
