#include <linux/init.h>
#include <linux/module.h>
#include <linux/gpio.h>
#include <linux/device.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/uaccess.h>

#define DEVICE_NAME "gpio_control"
#define CLASS_NAME "gpio"

static int major_number;
static struct class *gpio_class = NULL;
static struct device *gpio_device = NULL;
static int gpio_pin = 18; // Default GPIO pin

static int __init gpio_init(void) {
    major_number = register_chrdev(0, DEVICE_NAME, &fops);
    if (major_number < 0) {
        pr_err("Failed to register device\n");
        return major_number;
    }

    gpio_class = class_create(THIS_MODULE, CLASS_NAME);
    if (IS_ERR(gpio_class)) {
        unregister_chrdev(major_number, DEVICE_NAME);
        pr_err("Failed to create class\n");
        return PTR_ERR(gpio_class);
    }

    gpio_device = device_create(gpio_class, NULL, MKDEV(major_number, 0), NULL, DEVICE_NAME);
    if (IS_ERR(gpio_device)) {
        class_destroy(gpio_class);
        unregister_chrdev(major_number, DEVICE_NAME);
        pr_err("Failed to create device\n");
        return PTR_ERR(gpio_device);
    }

    if (gpio_request(gpio_pin, "relay_control") < 0) {
        pr_err("Failed to request GPIO pin\n");
        return -1;
    }
    gpio_direction_output(gpio_pin, 0);

    pr_info("GPIO module loaded\n");
    return 0;
}

static void __exit gpio_exit(void) {
    gpio_set_value(gpio_pin, 0);
    gpio_free(gpio_pin);
    device_destroy(gpio_class, MKDEV(major_number, 0));
    class_unregister(gpio_class);
    class_destroy(gpio_class);
    unregister_chrdev(major_number, DEVICE_NAME);
    pr_info("GPIO module unloaded\n");
}

module_init(gpio_init);
module_exit(gpio_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("Enhanced Kernel Module for GPIO Control");