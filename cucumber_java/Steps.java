package features;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import io.cucumber.java.After;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
public class Steps {
      WebDriver driver; 
     
    @Given("^I use the calculator$")
    public void i_use() throws Exception {
    driver = new ChromeDriver();
    System.setProperty("webdriver.chrome.driver", "C\\chromedriver.exe");
    driver.navigate().to("https://www.calculator.net/math-calculator.html");
    }
    @When("^I enter \"1\" into the calculator$")
            public void i_enter() throws Exception {
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[3]/span[1]")).click();
    }
    @And("^I add \"200\"$")
    public void i_add() throws Exception {
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[1]/span[4]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[3]/span[2]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[4]/span[1]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[4]/span[1]")).click();
    }    
    @And("^I subtract \"200\"$")
    public void i_subtract() throws Exception {
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[2]/span[4]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[3]/span[2]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[4]/span[1]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[4]/span[1]")).click();
    }   
    @And("^I divide by \"555\"$")
    public void i_divide() throws Exception {
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[4]/span[4]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[2]/span[2]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[2]/span[2]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[2]/span[2]")).click();
    }   
    @And("^I multiply by \"555\"$")
    public void i_multiply() throws Exception {
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[3]/span[4]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[2]/span[2]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[2]/span[2]")).click();
    	driver.findElement(By.xpath("//*[@id=\"sciout\"]/div[2]/div[2]/span[2]")).click();
    }   
    @Then("^the calculated result is \"1\"$")
	public void i_verify() throws Exception {
    	String appTitle1 = driver.findElement(By.id("sciOutPut")).getText();
    	assertEquals("1", appTitle1);
	}   
     @After
        public void tearDown() {
            driver.close();
        }
     
             
}