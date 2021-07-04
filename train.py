epochs = 50 # Increase the number of epochs for better results

gan = GAN(discriminator=discriminator, generator=generator, latent_dim=latent_dim)
gan.compile(
    d_optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    g_optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    loss_fn=keras.losses.BinaryCrossentropy(),
)

r=gan.fit(
    dataset, epochs=epochs, callbacks=[GANMonitor(num_img=10, latent_dim=latent_dim)]
)
#Plot the evaluation results
plt.plot(r.history['loss_fn'], label='d_loss')
plt.plot(r.history['loss_fn'], label='g_loss')
plt.legend()
plt.show()
plt.savefig('LossVal_loss')
