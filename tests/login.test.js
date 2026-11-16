import { describe, expect, it } from "vitest";
import { TestDriver } from "testdriverai/vitest/hooks";

describe("Login Flow", () => {
  it("should log in successfully with valid credentials", async (context) => {
    const testdriver = TestDriver(context);

    await testdriver.provision.chrome({ url: "https://www.saucedemo.com" });

    await testdriver.find("Username input field").click();
    await testdriver.type("standard_user");

    await testdriver.find("Password input field").click();
    await testdriver.type("secret_sauce");

    await testdriver.find("Login button").click();

    const assertResult = await testdriver.assert(
      "The Products title is displayed and inventory items are visible"
    );
    expect(assertResult).toBeTruthy();
  });
});
