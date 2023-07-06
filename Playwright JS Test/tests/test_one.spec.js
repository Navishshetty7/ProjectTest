import { test, expect } from '@playwright/test';

test('test amazon', async ({ page }) => {
  await page.goto('https://www.amazon.in/');
  await page.locator('id=twotabsearchtextbox').fill('Iphone 14');
  await page.locator('id=nav-search-submit-button').click();
  await page.getByRole('heading', { name: 'Apple iPhone 14 (128 GB) - Midnight' }).getByRole('link', { name: 'Apple iPhone 14 (128 GB) - Midnight' }).click();
  const page1Promise = page.waitForEvent('popup');
  const page1 = await page1Promise;
  await expect(page1.locator('xpath=//span[@class ="selection" and text()="128 GB"]')).toHaveCount(1);
  await expect(page1.locator('xpath=//span[@class ="selection" and text()="Midnight"]')).toHaveCount(1);
  await expect(page1.locator('xpath=//span[@class ="a-size-base po-break-word" and text()="Apple"]')).toHaveCount(1);
  await page.close();
  
});